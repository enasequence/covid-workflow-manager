import { __decorate } from "tslib";
import { Component } from '@angular/core';
let OntSamplesDetailsComponent = class OntSamplesDetailsComponent {
    constructor(route, title, dataService, sanitizer) {
        this.route = route;
        this.title = title;
        this.dataService = dataService;
        this.sanitizer = sanitizer;
    }
    ngOnInit() {
        this.title.setTitle('ONT Sample Logs details');
        this.route.params.subscribe((params) => {
            this.sampleId = params.id;
            this.reportLink = `http://193.62.54.246/nextflow_reports/${this.sampleId}_output/${this.sampleId}.html`;
            this.dataService.getSampleONT(this.sampleId).subscribe(data => {
                this.data = data.results;
            }, error => {
                console.log(error);
            });
        });
    }
    generateReport() {
        return this.sanitizer.bypassSecurityTrustResourceUrl(`http://193.62.54.246/nextflow_reports/${this.sampleId}_output/${this.sampleId}.html`);
    }
};
OntSamplesDetailsComponent = __decorate([
    Component({
        selector: 'app-ont-samples-details',
        templateUrl: './ont-samples-details.component.html',
        styleUrls: ['./ont-samples-details.component.css']
    })
], OntSamplesDetailsComponent);
export { OntSamplesDetailsComponent };
//# sourceMappingURL=ont-samples-details.component.js.map