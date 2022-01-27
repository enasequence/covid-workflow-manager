import { __decorate } from "tslib";
import { Component } from '@angular/core';
let FilteredSamplesComponent = class FilteredSamplesComponent {
    constructor(route, title, dataService) {
        this.route = route;
        this.title = title;
        this.dataService = dataService;
        this.p = 1;
        this.statuses = {
            ena_import: {
                success: 'download finished',
                failed: 'download failed'
            },
            pipeline_analysis: {
                success: 'pipeline_finished',
                started: 'pipeline_started'
            },
            ena_export: {
                success: 'export_finished',
                started: 'export_started'
            }
        };
    }
    ngOnInit() {
        this.title.setTitle('ONT Samples Logs filtered');
        this.route.params.subscribe((params) => {
            this.stage = params.stage;
            this.status = params.status;
            this.dataService.getFilteredSamplesONT(this.stage, this.status).subscribe(data => {
                this.data = data.results;
                console.log(data);
            }, error => {
                console.log(error);
            });
        });
    }
    getDate(item) {
        return item.split('-')[0];
    }
    getExportStatus(item, statusType) {
        if (item.indexOf(this.statuses[statusType].success) !== -1) {
            return 'Success';
        }
        else if (item.indexOf(this.statuses[statusType].started) !== -1) {
            if (this.getAllIndices(item, this.statuses[statusType].started).length >= 6) {
                return 'Failed';
            }
            return 'Processing';
        }
        else {
            return 'Undefined';
        }
    }
    getAllIndices(arr, val) {
        const indices = [];
        let i = -1;
        while (arr.indexOf(val, i + 1) !== -1) {
            i = arr.indexOf(val, i + 1);
            indices.push(i);
        }
        return indices;
    }
    getExportStatusClass(item, statusType) {
        if (item.indexOf(this.statuses[statusType].success) !== -1) {
            return 'badge badge-pill badge-success';
        }
        else if (item.indexOf(this.statuses[statusType].started) !== -1) {
            if (this.getAllIndices(item, this.statuses[statusType].started).length >= 6) {
                return 'badge badge-pill badge-danger';
            }
            return 'badge badge-pill badge-warning';
        }
        else {
            return 'badge badge-pill badge-info';
        }
    }
};
FilteredSamplesComponent = __decorate([
    Component({
        selector: 'app-filtered-samples',
        templateUrl: './filtered-samples.component.html',
    })
], FilteredSamplesComponent);
export { FilteredSamplesComponent };
//# sourceMappingURL=filtered-samples.component.js.map