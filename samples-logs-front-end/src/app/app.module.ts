import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SamplesDetailsComponent } from './samples-details/samples-details.component';
import { HeaderComponent } from './header/header.component';
import { SamplesComponent } from './samples/samples.component';
import {NgxPaginationModule} from 'ngx-pagination';
import {ApiDataService} from './services/api-data.service';
import {HttpClientModule} from '@angular/common/http';
import { OntSamplesComponent } from './ont-samples/ont-samples.component';
import { OntSamplesDetailsComponent } from './ont-samples-details/ont-samples-details.component';
import { OntSamplesFiltersComponent } from './ont-samples-filters/ont-samples-filters.component';

@NgModule({
  declarations: [
    AppComponent,
    SamplesDetailsComponent,
    HeaderComponent,
    SamplesComponent,
    OntSamplesComponent,
    OntSamplesDetailsComponent,
    OntSamplesFiltersComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgxPaginationModule,
    HttpClientModule
  ],
  providers: [ApiDataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
