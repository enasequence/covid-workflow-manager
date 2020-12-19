import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SamplesDetailsComponent } from './pages/samples-details/samples-details.component';
import { HeaderComponent } from './components/header/header.component';
import { SamplesComponent } from './pages/samples/samples.component';
import { NgxPaginationModule } from 'ngx-pagination';
import { HttpClientModule } from '@angular/common/http';
import { OntSamplesDetailsComponent } from './pages/ont-samples-details/ont-samples-details.component';
import { FilteredSamplesComponent } from './pages/filtered-samples/filtered-samples.component';
import { NavigationComponent } from './components/navigation/navigation.component';
import { JobStatusComponent } from './components/sample-table/job-status/job-status.component';
import { StatusFilterComponent } from './components/filter/status-filter/status-filter.component';
import { FilterPaneComponent } from './components/filter/filter-pane/filter-pane.component';
import { SampleTableComponent } from './components/sample-table/sample-table/sample-table.component';
import { environment } from 'src/environments/environment';

@NgModule({
  declarations: [
    AppComponent,
    SamplesDetailsComponent,
    HeaderComponent,
    SamplesComponent,
    OntSamplesDetailsComponent,
    FilteredSamplesComponent,
    NavigationComponent,
    JobStatusComponent,
    StatusFilterComponent,
    FilterPaneComponent,
    SampleTableComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgxPaginationModule,
    HttpClientModule
  ],
  providers: [
    ...environment.providers,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
