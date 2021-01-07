import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Title } from '@angular/platform-browser';
import { ApiService } from '@services/api.service';

@Component({
  selector: 'app-filtered-samples',
  templateUrl: './filtered-samples.component.html',
})
export class FilteredSamplesComponent implements OnInit {
  stage: string;
  status: string;
  data: any;
  p = 1;

  constructor(
    private route: ActivatedRoute,
    private title: Title,
    private dataService: ApiService
  ) { }

  ngOnInit() {
    this.title.setTitle('ONT Samples Logs filtered');
    this.route.params.subscribe(
      (params: Params) => {
        this.stage = params.stage;
        this.status = params.status;
        // this.dataService.getFilteredSamplesONT(this.stage, this.status).subscribe(
        //   data => {
        //     this.data = data.results;
        //   },
        //   error => {
        //     console.log(error);
        //   }
        // );
    });
  }

}
