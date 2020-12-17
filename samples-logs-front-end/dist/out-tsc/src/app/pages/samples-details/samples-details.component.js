import { __decorate } from "tslib";
import { Component } from '@angular/core';
let SamplesDetailsComponent = class SamplesDetailsComponent {
    constructor(route, title, dataService) {
        this.route = route;
        this.title = title;
        this.dataService = dataService;
    }
    ngOnInit() {
        this.title.setTitle('Sample Logs details');
        this.route.params.subscribe((params) => {
            this.sampleId = params.id;
            this.dataService.getSampleJovian(this.sampleId).subscribe(data => {
                this.data = data.results;
            }, error => {
                console.log(error);
            });
        });
    }
};
SamplesDetailsComponent = __decorate([
    Component({
        selector: 'app-samples-details',
        templateUrl: './samples-details.component.html',
        styleUrls: ['./samples-details.component.css']
    })
], SamplesDetailsComponent);
export { SamplesDetailsComponent };
//# sourceMappingURL=samples-details.component.js.map