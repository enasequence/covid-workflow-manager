import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SamplesDetailsComponent } from './pages/samples-details/samples-details.component';
import { HeaderComponent } from './components/header/header.component';
import { SamplesComponent } from './pages/samples/samples.component';
import { NgxPaginationModule } from 'ngx-pagination';
import { ApiDataService } from './services/api-data.service';
import { HttpClientModule } from '@angular/common/http';
import { OntSamplesComponent } from './pages/ont-samples/ont-samples.component';
import { OntSamplesDetailsComponent } from './pages/ont-samples-details/ont-samples-details.component';
import { FilteredSamplesComponent } from './pages/filtered-samples/filtered-samples.component';
import { SamplesNavigationComponent } from './components/samples-navigation/samples-navigation.component';
import { MockApiDataService } from '@services/mock-api-data.service';
import { JobStatusComponent } from './components/job-status/job-status.component';
import { StatusSummariesComponent } from './components/filter/status-summaries/status-summaries.component';
import { FilterPaneComponent } from './components/filter/filter-pane/filter-pane.component';

@NgModule({
  declarations: [
    AppComponent,
    SamplesDetailsComponent,
    HeaderComponent,
    SamplesComponent,
    OntSamplesComponent,
    OntSamplesDetailsComponent,
    FilteredSamplesComponent,
    SamplesNavigationComponent,
    JobStatusComponent,
    StatusSummariesComponent,
    FilterPaneComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgxPaginationModule,
    HttpClientModule
  ],
  providers: [
    ApiDataService,
    MockApiDataService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
