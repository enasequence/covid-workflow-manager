import { Injectable } from '@angular/core';

import { get, map, includes, flow, split, head, cond, constant, stubTrue, countBy, eq, gte, identity, tap } from 'lodash/fp';
import { curry } from 'lodash/fp';

import { ApiResponse } from '@models/api';
import { SampleLog } from '@models/sample-log';
import { JobStatus } from '@models/job-status';
import { CurrencyPipe } from '@angular/common';

@Injectable({
  providedIn: 'root'
})
export class TransformService {

  constructor() { }

  // extractPipelinStatus = curry();

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

  summarise(data: SampleLog[]) {
    const countUniqueStrings = countBy(identity());
    return {
      import: flow(map('importStatus'), countUniqueStrings)(data),
      pipeline: flow(map('pipelineStatus'), countUniqueStrings)(data),
      export: flow(map('exportStatus'), countUniqueStrings)(data)
    };
  }

}
