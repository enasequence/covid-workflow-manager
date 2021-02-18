import { Observable } from 'rxjs';

import { ApiResponse } from '@models/api';
import { SampleLog } from '@models/sample-log';

export interface DataProvider {
    getSamples(path, params): Observable<SampleLog[]>;
    getSample(pipeline, id): Observable<SampleLog>;

}
