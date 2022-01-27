import { __decorate } from "tslib";
import { Component, Input } from '@angular/core';
let FilterPaneComponent = class FilterPaneComponent {
    constructor() { }
    getImport() {
        return this.summary.import;
    }
    ngOnInit() {
    }
};
__decorate([
    Input()
], FilterPaneComponent.prototype, "summary", void 0);
FilterPaneComponent = __decorate([
    Component({
        selector: 'app-filter-pane',
        templateUrl: './filter-pane.component.html',
    })
], FilterPaneComponent);
export { FilterPaneComponent };
//# sourceMappingURL=filter-pane.component.js.map