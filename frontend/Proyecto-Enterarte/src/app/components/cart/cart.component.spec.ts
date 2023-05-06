import { ComponentFixture, TestBed } from '@angular/core/testing';

import { cartComponent } from './cart.component';

describe('cartComponent', () => {
  let component: cartComponent;
  let fixture: ComponentFixture<cartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ cartComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(cartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
