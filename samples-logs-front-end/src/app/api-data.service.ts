import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import {throwError} from 'rxjs';
import { catchError, retry, map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiDataService {

  constructor(private http: HttpClient) { }

  getAllSamplesJovian() {
    return this.http.get<any>('http://193.62.54.246/api/jovian').pipe(
      retry(3),
      catchError(this.handleError),
    );
  }

  getSampleJovian(id: string) {
    const url = `http://193.62.54.246/api/jovian/${id}`;
    return this.http.get<any>(url).pipe(
      retry(3),
      catchError(this.handleError)
    );
  }

  getAllSamplesONT() {
    return this.http.get<any>('http://193.62.54.246/api/ont').pipe(
      retry(3),
      catchError(this.handleError),
    );
  }

  getSampleONT(id: string) {
    const url = `http://193.62.54.246/api/ont/${id}`;
    return this.http.get<any>(url).pipe(
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
