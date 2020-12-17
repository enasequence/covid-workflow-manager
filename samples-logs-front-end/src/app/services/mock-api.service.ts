import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import jovian from './mock/jovian-mock.json';
import jovian2 from './mock/jovian-mock-2.json';
import ont from './mock/ont-mock.json';
import ont2 from './mock/ont-mock-2.json';
import job from './mock/job-mock.json';

@Injectable({
  providedIn: 'root'
})
export class MockApiService {

  constructor() { }

  getMockJovianSamples(): Observable<any> {
    return of(jovian);
  }

  getMockSample(): Observable<any> {
    return of(job);
  }

  getMockOntSamples(): Observable<any> {
    return of(ont);
  }

}
