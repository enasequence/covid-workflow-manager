import { async, TestBed } from '@angular/core/testing';
import { SamplesNavigationComponent } from './samples-navigation.component';
describe('SamplesNavigationComponent', () => {
    let component;
    let fixture;
    beforeEach(async(() => {
        TestBed.configureTestingModule({
            declarations: [SamplesNavigationComponent]
        })
            .compileComponents();
    }));
    beforeEach(() => {
        fixture = TestBed.createComponent(SamplesNavigationComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });
    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
//# sourceMappingURL=samples-navigation.component.spec.js.map