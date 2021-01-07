import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { Observable, of } from 'rxjs';

import { DataProvider } from './data-provider';

import jovian from './mock-data/jovian-mock.json';
import jovian2 from './mock-data/jovian-mock-2.json';
import ont from './mock-data/ont-mock.json';
import ont2 from './mock-data/ont-mock-2.json';
import job from './mock-data/job-mock.json';

@Injectable({
  providedIn: 'root'
})
export class ApiService implements DataProvider {

  constructor(
    private http: HttpClient
  ) { }

  get(path: string, params: HttpParams = new HttpParams()): Observable<any> {
    switch (path) {
      case 'jovian':
        return of(jovian);
      case 'ont':
        return of(ont);
      case 'jovian_test':
        return this.http.get<any>(environment.apiUrl + path, { params });
      default:
        return of(ont2);
    }
  }

  getSample(pipeline: string, id: string): Observable<any> {
    return of(job);
  }

  getMockSample(): Observable<any> {
    return of(job);
  }

}
