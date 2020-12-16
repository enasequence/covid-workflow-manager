import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {AppComponent} from './app.component';
import {SamplesDetailsComponent} from './pages/samples-details/samples-details.component';
import {SamplesComponent} from './pages/samples/samples.component';
import {OntSamplesComponent} from './pages/ont-samples/ont-samples.component';
import {OntSamplesDetailsComponent} from './pages/ont-samples-details/ont-samples-details.component';
import {FilteredSamplesComponent} from './pages/filtered-samples/filtered-samples.component';


const routes: Routes = [
  {path: '', redirectTo: 'jovian', pathMatch: 'full'},
  {path: 'jovian', component: SamplesComponent},
  {path: 'jovian/:id', component: SamplesDetailsComponent},
  {path: 'ont', component: OntSamplesComponent},
  {path: 'ont/:id', component: OntSamplesDetailsComponent},
  {path: 'ont/:stage/:status', component: FilteredSamplesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
