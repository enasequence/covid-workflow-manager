import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { map as _map, get, includes, flow, split, head, cond, constant, stubTrue, countBy, eq, gte, identity, filter } from 'lodash/fp';

import { SampleLog } from '@models/sample-log';
import { JobStatus } from '@models/job-status';
import { ApiService } from './api-mock.service';

@Injectable({
  providedIn: 'root'
})
export class TransformService {

  constructor(
    private apiService: ApiService,
  ) { }

  getSamples(pipeline: string): Observable<SampleLog[]> {
    switch (pipeline) {
      case 'jovian':
      case 'jovian_test':
        return this.apiService.getSamples(pipeline).pipe(
          map(this.extractJovianPipelineStatus),
        );
      case ('ont'):
        return this.apiService.getSamples(pipeline).pipe(
          map(this.extractOntPipelineStatus),
        );
      default:
        return this.apiService.getSamples(pipeline).pipe(
          map(this.extractOntPipelineStatus),
        );
    }
  }

  getFilteredSamples(pipeline: string, stage: string, status: string): Observable<SampleLog[]> {

    const otherwise = stubTrue;
    const parse = cond([
      [eq('import_from_ena'), constant('importStatus')],
      [eq('pipeline_analysis'), constant('pipelineStatus')],
      [eq('export_to_ena'), constant('exportStatus')],
      [otherwise, identity]
    ]);

    return this.getSamples(pipeline).pipe(
      map(filter([parse(stage), parse(status)])),
    );
  }

  extractJovianPipelineStatus(response: any): SampleLog[] {
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

    return response.map(result => ({
        id: result.id,
        sampleId: result.sample_id,
        studyId: result.study_id,
        pipeline: result.pipeline_name,
        date: getDate(result),
        importStatus: calculateImportStatus(result),
        pipelineStatus: calculatePipelineStatus(result),
        exportStatus: calculateExportStatus(result),
      }));
  }

  extractOntPipelineStatus(response: any): SampleLog[] {
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

    return response.map(result => ({
        id: result.id,
        date: getDate(result),
        importStatus: calculateImportStatus(result),
        pipelineStatus: calculatePipelineStatus(result),
        exportStatus: calculateExportStatus(result)
      }));
  }

  summarise(data: SampleLog[]) {
    const countUniqueStrings = countBy(identity());
    return {
      import: flow(_map('importStatus'), countUniqueStrings)(data),
      pipeline: flow(_map('pipelineStatus'), countUniqueStrings)(data),
      export: flow(_map('exportStatus'), countUniqueStrings)(data)
    };
  }

}