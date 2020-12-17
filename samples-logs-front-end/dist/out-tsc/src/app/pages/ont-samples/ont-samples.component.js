import { __decorate } from "tslib";
import { Component } from '@angular/core';
import { map } from 'rxjs/operators';
let OntSamplesComponent = class OntSamplesComponent {
    constructor(title, dataService, mock) {
        this.title = title;
        this.dataService = dataService;
        this.mock = mock;
        this.p = 1;
    }
    ngOnInit() {
        this.title.setTitle('Nanopore Sample Logs');
        // this.dataService.getAllSamplesONT().subscribe(
        //   data => {
        //     this.data = data.results;
        //     if (this.data) {
        //       this.getSummary(data.results);
        //     }
        //   },
        //   error => {
        //     console.log(error);
        //   }
        // );
        this.mock.getMockOntSamples()
            .pipe(map(this.dataService.extractOntPipelineStatus)).subscribe(parsedData => {
            this.data = parsedData;
            this.summary = this.dataService.summariseStatuses(parsedData);
        });
    }
};
OntSamplesComponent = __decorate([
    Component({
        selector: 'app-ont-samples',
        templateUrl: './ont-samples.component.html',
        styleUrls: ['./ont-samples.component.css']
    })
], OntSamplesComponent);
export { OntSamplesComponent };
//# sourceMappingURL=ont-samples.component.js.map