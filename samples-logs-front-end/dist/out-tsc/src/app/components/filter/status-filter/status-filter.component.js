import { __decorate } from "tslib";
import { Component, Input } from '@angular/core';
import { get } from 'lodash/fp';
let StatusFilterComponent = class StatusFilterComponent {
    constructor() { }
    getStatuses(stage) {
        return get(stage)(this.summary);
    }
    ngOnInit() {
    }
};
__decorate([
    Input()
], StatusFilterComponent.prototype, "stage", void 0);
__decorate([
    Input()
], StatusFilterComponent.prototype, "summary", void 0);
StatusFilterComponent = __decorate([
    Component({
        selector: 'app-status-filter',
        templateUrl: './status-filter.component.html',
    })
], StatusFilterComponent);
export { StatusFilterComponent };
//# sourceMappingURL=status-filter.component.js.map