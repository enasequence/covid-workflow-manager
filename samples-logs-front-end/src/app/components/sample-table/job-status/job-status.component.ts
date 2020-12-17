import { Component, Input, OnInit } from '@angular/core';
import { JobStatus } from '@models/job-status';

@Component({
  selector: 'app-job-status',
  templateUrl: './job-status.component.html',
  styleUrls: ['./job-status.component.css']
})
export class JobStatusComponent implements OnInit {

  @Input() public status: JobStatus = JobStatus.Undefined;

  constructor() { }

  ngOnInit() {
  }

  public getStatusClass(status: JobStatus): string {
    switch (status as JobStatus) {
      case JobStatus.Success:
        return 'badge badge-pill badge-success';
      case JobStatus.Processing:
        return 'badge badge-pill badge-warning';
      case JobStatus.Failed:
        return 'badge badge-pill badge-danger';
      case JobStatus.Undefined:
        return 'badge badge-pill badge-info';
      default:
        return 'badge badge-pill badge-secondary';
    }
  }

}
