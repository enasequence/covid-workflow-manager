import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FilteredSamplesComponent } from './filtered-samples.component';

describe('FilteredSamplesComponent', () => {
  let component: FilteredSamplesComponent;
  let fixture: ComponentFixture<FilteredSamplesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FilteredSamplesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FilteredSamplesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
