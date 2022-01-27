import { __decorate } from "tslib";
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { SamplesDetailsComponent } from './pages/samples-details/samples-details.component';
import { SamplesComponent } from './pages/samples/samples.component';
import { OntSamplesComponent } from './pages/ont-samples/ont-samples.component';
import { OntSamplesDetailsComponent } from './pages/ont-samples-details/ont-samples-details.component';
import { FilteredSamplesComponent } from './pages/filtered-samples/filtered-samples.component';
const routes = [
    { path: '', redirectTo: 'jovian', pathMatch: 'full' },
    { path: 'jovian', component: SamplesComponent },
    { path: 'jovian/:id', component: SamplesDetailsComponent },
    { path: 'ont', component: OntSamplesComponent },
    { path: 'ont/:id', component: OntSamplesDetailsComponent },
    { path: 'ont/:stage/:status', component: FilteredSamplesComponent }
];
let AppRoutingModule = class AppRoutingModule {
};
AppRoutingModule = __decorate([
    NgModule({
        imports: [RouterModule.forRoot(routes)],
        exports: [RouterModule]
    })
], AppRoutingModule);
export { AppRoutingModule };
//# sourceMappingURL=app-routing.module.js.map