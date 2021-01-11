import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SamplesDetailsComponent } from './pages/samples-details/samples-details.component';
import { HeaderComponent } from './components/header/header.component';
import { SamplesComponent } from './pages/samples/samples.component';
import { NgxPaginationModule } from 'ngx-pagination';
import { HttpClientModule } from '@angular/common/http';
import { FilteredSamplesComponent } from './pages/filtered-samples/filtered-samples.component';
import { NavigationComponent } from './components/navigation/navigation.component';
import { JobStatusComponent } from './components/sample-table/job-status/job-status.component';
import { StatusFilterComponent } from './components/filter/status-filter/status-filter.component';
import { FilterPaneComponent } from './components/filter/filter-pane/filter-pane.component';
import { SampleTableComponent } from './components/sample-table/sample-table/sample-table.component';
import { environment } from 'src/environments/environment';
import { FooterComponent } from './components/footer/footer.component';
import { LogListComponent } from './components/log-list/log-list.component';
import { ErrorComponent } from './pages/error/error.component';

@NgModule({
  declarations: [
    AppComponent,
    SamplesComponent,
    FilteredSamplesComponent,
    SamplesDetailsComponent,
    HeaderComponent,
    FooterComponent,
    SampleTableComponent,
    NavigationComponent,
    FilterPaneComponent,
    StatusFilterComponent,
    JobStatusComponent,
    LogListComponent,
    ErrorComponent,
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
