import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {AppComponent} from './app.component';
import {SamplesDetailsComponent} from './samples-details/samples-details.component';
import {SamplesComponent} from './samples/samples.component';
import {OntSamplesComponent} from './ont-samples/ont-samples.component';
import {OntSamplesDetailsComponent} from './ont-samples-details/ont-samples-details.component';
import {OntSamplesFiltersComponent} from './ont-samples-filters/ont-samples-filters.component';


const routes: Routes = [
  {path: '', redirectTo: 'jovian', pathMatch: 'full'},
  {path: 'jovian', component: SamplesComponent},
  {path: 'jovian/:id', component: SamplesDetailsComponent},
  {path: 'ont', component: OntSamplesComponent},
  {path: 'ont/:id', component: OntSamplesDetailsComponent},
  {path: 'ont/:stage/:status', component: OntSamplesFiltersComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
