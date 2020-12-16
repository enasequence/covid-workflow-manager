import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StatusSummariesComponent } from './status-summaries.component';

describe('StatusSummaryComponent', () => {
  let component: StatusSummariesComponent;
  let fixture: ComponentFixture<StatusSummariesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StatusSummariesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StatusSummariesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
