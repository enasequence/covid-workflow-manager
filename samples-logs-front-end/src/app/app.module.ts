import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SamplesDetailsComponent } from './samples-details/samples-details.component';
import { HeaderComponent } from './header/header.component';
import { SamplesComponent } from './samples/samples.component';
import {NgxPaginationModule} from "ngx-pagination";
import {ApiDataService} from "./api-data.service";

@NgModule({
  declarations: [
    AppComponent,
    SamplesDetailsComponent,
    HeaderComponent,
    SamplesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgxPaginationModule
  ],
  providers: [ApiDataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
