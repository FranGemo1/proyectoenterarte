import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FdepagosComponent } from './fdepagos.component';

describe('FdepagosComponent', () => {
  let component: FdepagosComponent;
  let fixture: ComponentFixture<FdepagosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FdepagosComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FdepagosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
