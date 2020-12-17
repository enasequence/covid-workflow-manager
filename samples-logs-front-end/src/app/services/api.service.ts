import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

import { get, map, includes, flow, split, head, cond, constant, stubTrue, countBy, eq, gte, identity, tap } from 'lodash/fp';

import { ApiResponse } from '@models/api';
import { SampleLog } from '@models/sample-log';
import { JobStatus } from '@models/job-status';
import { apiUrl } from '@services/api-url';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  getAllSamplesJovian() {
    return this.http.get<ApiResponse>(apiUrl('jovian_test')).pipe(
      retry(3),
      catchError(this.handleError),
    );
  }

  extractJovianPipelineStatus(response: ApiResponse): SampleLog[] {
    const otherwise = stubTrue;
    const getDate = flow(
      get('import_from_ena.date[0]'),
      split(' - '),
      head
    );

    const calculateImportStatus = flow(
      get('import_from_ena.status'),
      cond([
        [includes('download finished'), constant(JobStatus.Success)],
        [includes('download failed'), constant(JobStatus.Failed)],
        [otherwise, constant(JobStatus.Undefined)]
      ]));

    const calculatePipelineStatus = flow(
      get('pipeline_analysis.status'),
      cond([
        [includes('pipeline finished'), constant(JobStatus.Success)],
        [includes('pipeline finished with errors'), constant(JobStatus.Failed)],
        [otherwise, constant(JobStatus.Undefined)]
      ]));

    const calculateExportStatus = flow(
      get('export_to_ena.status'),
      cond([
        [includes('submission to ENA finished'), constant(JobStatus.Success)],
        [includes('submission to ENA failed'), constant(JobStatus.Failed)],
        [otherwise, constant(JobStatus.Undefined)]
      ]));

    return flow(
      get('results'),
      map(result => ({
        id: result.id,
        sampleId: result.sample_id,
        studyId: result.study_id,
        pipeline: result.pipeline_name,
        date: getDate(result),
        importStatus: calculateImportStatus(result),
        pipeStatus: calculatePipelineStatus(result),
        exportStatus: calculateExportStatus(result),
      }))
    )(response);
  }

  getSampleJovian(id: string) {
    return this.http.get<any>(apiUrl('jovian', id)).pipe(
      retry(3),
      catchError(this.handleError)
    );
  }

  getAllSamplesONT() {
    return this.http.get<any>(apiUrl('ont')).pipe(
      retry(3),
      catchError(this.handleError),
    );
  }

  extractOntPipelineStatus(response: ApiResponse): SampleLog[] {
    const otherwise = stubTrue;
    const hasPipelineErrors = flow(
      countBy(eq('pipeline_started')),
      gte(5));
    const hasExportErrors = flow(
      countBy(eq('export_started')),
      gte(5));
    const getDate = flow(
      get('import_from_ena.date[0]'),
      split(' - '),
      head
    );

    const calculateImportStatus = flow(
      get('import_from_ena.status'),
      cond([
        [includes('download finished'), constant(JobStatus.Success)],
        [includes('download failed'), constant(JobStatus.Failed)],
        [otherwise, constant(JobStatus.Undefined)]
      ]));

    const calculatePipelineStatus = flow(
      get('pipeline_analysis.status'),
      cond([
        [includes('pipeline_finished'), constant(JobStatus.Success)],
        [hasPipelineErrors, constant(JobStatus.Failed)],
        [includes('pipeline_started'), constant(JobStatus.Processing)],
        [otherwise, constant(JobStatus.Undefined)]
      ]));

    const calculateExportStatus = flow(
      get('export_to_ena.status'),
      cond([
        [includes('export_finished'), constant(JobStatus.Success)],
        [hasExportErrors, constant(JobStatus.Failed)],
        [includes('export_started'), constant(JobStatus.Processing)],
        [otherwise, constant(JobStatus.Undefined)]
      ]));

    return flow(
      get('results'),
      map(result => ({
        id: result.id,
        date: getDate(result),
        importStatus: calculateImportStatus(result),
        pipelineStatus: calculatePipelineStatus(result),
        exportStatus: calculateExportStatus(result)
      })))(response);
  }

  summariseStatuses(data: SampleLog[]) {
    const countUniqueStrings = countBy(identity());
    return {
      import: flow(map('importStatus'), countUniqueStrings)(data),
      pipeline: flow(map('pipelineStatus'), countUniqueStrings)(data),
      export: flow(map('exportStatus'), countUniqueStrings)(data)
    };
  }

  getFilteredSamplesONT(stage: string, status: string) {
    return this.http.get<any>(apiUrl('ont', stage, status)).pipe(
      retry(3),
      catchError(this.handleError)
    );
  }

  getSampleONT(id: string) {
    return this.http.get<any>(apiUrl('ont', id)).pipe(
      retry(3),
      catchError(this.handleError)
    );
  }


  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      console.error(
        'A client-side or network error occurred',
         error.error.message);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong,
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
      console.error(error);
    }
    // return an observable with a user-facing errorSubject message
    return throwError(
      'Something bad happened; please try again later.');
  }
}
