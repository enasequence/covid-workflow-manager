import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SamplesDetailsComponent } from './samples-details.component';

describe('SamplesDetailsComponent', () => {
  let component: SamplesDetailsComponent;
  let fixture: ComponentFixture<SamplesDetailsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SamplesDetailsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SamplesDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
