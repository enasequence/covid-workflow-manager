import { Observable } from 'rxjs';

import { ApiResponse } from '@models/api';

export interface DataProvider {
    get(path, params): Observable<ApiResponse>;

}
