import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { throwError, of } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

import { apiUrl } from '@services/api-url';
import data from './jovian-mock.json';

@Injectable({
  providedIn: 'root'
})
export class ApiDataService {

  constructor(private http: HttpClient) { }

  getAllSamplesJovian() {
    return this.http.get<any>(apiUrl('jovian')).pipe(
      retry(3),
      catchError(this.handleError),
    );
  }

  getMockJovianSamples() {
    return of(data);
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
      // A client-side or network errorSubject occurred. Handle it accordingly.
      console.error('An errorSubject occurred:', error.error.message);
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
