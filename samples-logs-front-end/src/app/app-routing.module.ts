import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { SamplesDetailsComponent } from './pages/samples-details/samples-details.component';
import { SamplesComponent } from './pages/samples/samples.component';
import { FilteredSamplesComponent } from './pages/filtered-samples/filtered-samples.component';


const routes: Routes = [
  { path: '', redirectTo: 'jovian', pathMatch: 'full' },
  { path: ':pipeline', component: SamplesComponent },
  { path: ':pipeline/:id', component: SamplesDetailsComponent },
  { path: ':pipeline/:stage/:status', component: FilteredSamplesComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
