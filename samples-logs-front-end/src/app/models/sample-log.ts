import JobStatus from './job-status';

export interface SampleLogCollection {
  date: string[];
  status: string[];
  errors: string[];
}

export interface SampleLog {
  id: string;
  sampleId?: string;
  studyId?: string;
  pipeline?: string;
  date: string;
  importStatus: JobStatus;
  pipeStatus: JobStatus;
  exportStatus: JobStatus;
}
