import { __decorate } from "tslib";
import { Injectable } from '@angular/core';
import { of } from 'rxjs';
import jovian from './mock/jovian-mock-2.json';
import ont from './mock/ont-mock-2.json';
import job from './mock/job-mock.json';
let MockApiDataService = class MockApiDataService {
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
};
MockApiDataService = __decorate([
    Injectable({
        providedIn: 'root'
    })
], MockApiDataService);
export { MockApiDataService };
//# sourceMappingURL=mock-api-data.service.js.map