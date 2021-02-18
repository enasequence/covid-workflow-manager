import { __decorate } from "tslib";
import { Component } from '@angular/core';
import { map } from 'rxjs/operators';
let SamplesComponent = class SamplesComponent {
    constructor(title, dataService, mock) {
        this.title = title;
        this.dataService = dataService;
        this.mock = mock;
        this.p = 1;
    }
    ngOnInit() {
        this.title.setTitle('Jovian Samples Logs');
        this.dataService.getAllSamplesJovian().pipe(map(this.dataService.extractJovianPipelineStatus)).subscribe(parsedData => {
            this.data = parsedData;
            this.summary = this.dataService.summariseStatuses(parsedData);
        }, error => {
            console.log(error);
        });
        // this.mock.getMockJovianSamples()
        //   .pipe(
        //     map(this.dataService.extractJovianPipelineStatus)
        //   ).subscribe(
        //   parsedData => {
        //   sdata = parsedData;
        //     this.summaryi.dataService.summariseStatuses(parsedData);
        //   
        // //
    }
};
SamplesComponent = __decorate([
    Component({
        selector: 'app-samples',
        templateUrl: './samples.component.html',
        styleUrls: ['./samples.component.css']
    })
], SamplesComponent);
export { SamplesComponent };
//# sourceMappingURL=samples.component.js.map