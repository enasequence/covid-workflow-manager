import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';


import { environment } from '../../environments/environment';
import { ApiResponse } from '@models/api';
import { DataProvider } from './data-provider';

@Injectable({
  providedIn: 'root'
})
export class ApiService implements DataProvider {

  constructor(private http: HttpClient) { }

  get(path: string, params: HttpParams = new HttpParams()): Observable<any> {
    return this.http.get<any>(environment.apiUrl + path, { params }).pipe(
      retry(3),
      catchError(this.handleError)
    );
  }

  getSample(pipeline: string, id: string) {
    return this.get(`${pipeline}/${id}`).pipe(
      retry(3),
      catchError(this.handleError)
    );
  }

  getSampleJovian(id: string) {
    return this.get(`jovian/${id}`).pipe(
      retry(3),
      catchError(this.handleError)
    );
  }

  getFilteredSamplesONT(stage: string, status: string): Observable<ApiResponse> {
    return this.get(`ont/${stage}/${status}`).pipe(
      retry(3),
      catchError(this.handleError)
    );
  }

  getSampleONT(id: string) {
    return this.get(`ont/${id}`).pipe(
      retry(3),
      catchError(this.handleError)
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
