import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { map, catchError, retry, shareReplay } from 'rxjs/operators';
import { get } from 'lodash/fp';

import { environment } from '../../environments/environment';
import { DataProvider } from './data-provider';
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

  getSamples(pipeline: string): Observable<any> {
    return this.get(pipeline)
      .pipe(
        map(get('results')),
        shareReplay(),
      );
  }

  getSample(pipeline: string, id: string): Observable<any> {
    return this.get(`${pipeline}/${id}`)
      .pipe(
        map(get('results')),
        shareReplay(),
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
