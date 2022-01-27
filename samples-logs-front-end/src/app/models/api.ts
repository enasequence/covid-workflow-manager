import { SampleLogCollection } from './sample-log';

export interface ApiResponse {
  results: ApiResult[];
}

export interface ApiResult {
  id: string;
  pipeline_name: string;
  sample_id: string;
  study_id: string;
  import_from_ena: SampleLogCollection;
  pipeline_analysis: SampleLogCollection;
  export_to_ena: SampleLogCollection;
}
