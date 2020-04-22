import { Component, OnInit } from '@angular/core';
import {Title} from "@angular/platform-browser";

@Component({
  selector: 'app-samples',
  templateUrl: './samples.component.html',
  styleUrls: ['./samples.component.css']
})
export class SamplesComponent implements OnInit {
  p: number = 1;
  data = [{'id': 'ERR3482174', 'export_from_ena': {'date': ['22 April, 2020 - 14:13:39', '22 April, 2020 - 14:13:39', '22 April, 2020 - 14:13:45'], 'status': ['run added for download', 'download started', 'download finished'], 'errors': ['--2020-04-22 14:13:39--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/004/ERR3482174/ERR3482174_1.fastq.gz\n           => ‘/raw_data/ERR3482174/ERR3482174_1.fastq.gz’\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\nLogging in as dcc_byard ... \nLogin incorrect.\n']}, 'pipeline_analysis': {'date': [], 'status': [], 'errors': []}, 'import_to_ena': {'date': [], 'status': [], 'errors': []}}, {'id': 'ERR3482177', 'export_from_ena': {'date': ['22 April, 2020 - 14:13:39', '22 April, 2020 - 14:13:45', '22 April, 2020 - 14:13:52'], 'status': ['run added for download', 'download started', 'download finished'], 'errors': []}, 'pipeline_analysis': {'date': [], 'status': [], 'errors': []}, 'import_to_ena': {'date': [], 'status': [], 'errors': []}}, {'id': 'ERR3482180', 'export_from_ena': {'date': ['22 April, 2020 - 14:13:39', '22 April, 2020 - 14:13:52', '22 April, 2020 - 14:14:18'], 'status': ['run added for download', 'download started', 'download finished'], 'errors': []}, 'pipeline_analysis': {'date': [], 'status': [], 'errors': []}, 'import_to_ena': {'date': [], 'status': [], 'errors': []}}, {'id': 'ERR3482181', 'export_from_ena': {'date': ['22 April, 2020 - 14:13:39', '22 April, 2020 - 14:14:18', '22 April, 2020 - 14:14:36'], 'status': ['run added for download', 'download started', 'download finished'], 'errors': ['--2020-04-22 14:14:18--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/001/ERR3482181/ERR3482181_1.fastq.gz\n           => ‘/raw_data/ERR3482181/ERR3482181_1.fastq.gz’\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\nLogging in as dcc_byard ... \nLogin incorrect.\n', '--2020-04-22 14:14:23--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/001/ERR3482181/ERR3482181_2.fastq.gz\n           => ‘/raw_data/ERR3482181/ERR3482181_2.fastq.gz’\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\nLogging in as dcc_byard ... \nLogin incorrect.\n', '--2020-04-22 14:14:26--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/001/ERR3482181/ERR3482181_2.fastq.gz\n           => ‘/raw_data/ERR3482181/ERR3482181_2.fastq.gz’\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\nLogging in as dcc_byard ... \nLogin incorrect.\n', '--2020-04-22 14:14:29--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/001/ERR3482181/ERR3482181_2.fastq.gz\n           => ‘/raw_data/ERR3482181/ERR3482181_2.fastq.gz’\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\nLogging in as dcc_byard ... \nLogin incorrect.\n', '--2020-04-22 14:14:32--  ftp://dcc_byard:*password*@ftp.dcc-private.ebi.ac.uk/vol1/fastq/ERR348/001/ERR3482181/ERR3482181_2.fastq.gz\n           => ‘/raw_data/ERR3482181/ERR3482181_2.fastq.gz’\nResolving ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)... 193.62.193.6\nConnecting to ftp.dcc-private.ebi.ac.uk (ftp.dcc-private.ebi.ac.uk)|193.62.193.6|:21... connected.\nLogging in as dcc_byard ... \nLogin incorrect.\n']}, 'pipeline_analysis': {'date': [], 'status': [], 'errors': []}, 'import_to_ena': {'date': [], 'status': [], 'errors': []}}, {'id': 'ERR3482182', 'export_from_ena': {'date': ['22 April, 2020 - 14:13:39', '22 April, 2020 - 14:14:36', '22 April, 2020 - 14:14:37'], 'status': ['run added for download', 'download started', 'download finished'], 'errors': []}, 'pipeline_analysis': {'date': [], 'status': [], 'errors': []}, 'import_to_ena': {'date': [], 'status': [], 'errors': []}}];

  constructor(private title: Title) { }

  ngOnInit() {
    this.title.setTitle('Samples Logs');
  }

  getDate(item: any) {
    return item.split('-')[0];
  }

  getExportStatus(item: any) {
    return item.indexOf('download finished') !== -1 ? 'Success' : 'Failed';
  }

  getExportStatusClass(item: any) {
    return item.indexOf('download finished') !== -1 ? 'badge badge-pill badge-success' : 'badge badge-pill badge-danger';
  }

}
