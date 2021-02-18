import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { Observable, of, throwError } from 'rxjs';

import { DataProvider } from './data-provider';
import { catchError, map, retry } from 'rxjs/operators';
import { get } from 'lodash/fp';

import jovian from './mock-data/jovian-mock.json';
import jovian2 from './mock-data/jovian-mock-2.json';
import ont from './mock-data/ont-mock.json';
import ont2 from './mock-data/ont-mock-2.json';
import job from './mock-data/job-mock.json';
import { SampleLog } from '@models/sample-log';

@Injectable({
  providedIn: 'root'
})
export class ApiService implements DataProvider {

  constructor(
    private http: HttpClient
  ) { }

  private get(path: string, params: HttpParams = new HttpParams()): Observable<unknown> {
    return this.http.get(environment.apiUrl + path, { params })
      .pipe(
        retry(3),
        catchError(this.handleError),
      );
  }

  getSamples(pipeline: string): Observable<SampleLog[]> {
    const getResults = get('results');
    switch (pipeline) {
      case 'jovian':
        return of(jovian).pipe(map(getResults));
      case 'jovian_test':
        return this.get(pipeline).pipe(map(getResults));
      case 'ont':
        return of(ont).pipe(map(getResults));
      default:
        return of(ont2).pipe(map(getResults));
    }
  }

  getSample(pipeline: string, id: string): Observable<SampleLog> {
    return of(job).pipe(map(get('results')));
  }

  private handleError(error: HttpErrorResponse) {
    console.error(error);
    return throwError('Something bad happened; please try again later.');
  }

}
