import { __decorate } from "tslib";
import { Component, Input } from '@angular/core';
import { JobStatus } from '../../../models/job-status';
let JobStatusComponent = class JobStatusComponent {
    constructor() {
        this.status = JobStatus.Undefined;
    }
    ngOnInit() {
    }
    getStatusClass(status) {
        switch (status) {
            case JobStatus.Success:
                return 'badge badge-pill badge-success';
            case JobStatus.Processing:
                return 'badge badge-pill badge-warning';
            case JobStatus.Failed:
                return 'badge badge-pill badge-danger';
            case JobStatus.Undefined:
                return 'badge badge-pill badge-info';
            default:
                throw new Error('Unrecognised job status');
        }
        ;
    }
};
__decorate([
    Input()
], JobStatusComponent.prototype, "status", void 0);
JobStatusComponent = __decorate([
    Component({
        selector: 'app-job-status',
        templateUrl: './job-status.component.html',
        styleUrls: ['./job-status.component.css']
    })
], JobStatusComponent);
export { JobStatusComponent };
//# sourceMappingURL=job-status.component.js.map