import { async, TestBed } from '@angular/core/testing';
import { FilterPaneComponent } from './filter-pane.component';
describe('FilterPaneComponent', () => {
    let component;
    let fixture;
    beforeEach(async(() => {
        TestBed.configureTestingModule({
            declarations: [FilterPaneComponent]
        })
            .compileComponents();
    }));
    beforeEach(() => {
        fixture = TestBed.createComponent(FilterPaneComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });
    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
//# sourceMappingURL=filter-pane.component.spec.js.map