import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import { ApiResult } from './api-data.service';
import jovian from './mock/jovian-mock-2.json';
import ont from './mock/ont-mock-2.json';
import job from './mock/job-mock.json';

interface Result {
  results: ApiResult[]
}

@Injectable({
  providedIn: 'root'
})
export class MockApiDataService {

  constructor() { }

  getMockJovianSamples() {
    return of(jovian);
  }

  getMockSample() {
    return of(job);
  }

  getMockOntSamples() {
    return of(ont);
  }

}
