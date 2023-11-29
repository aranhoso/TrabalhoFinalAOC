import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InstructionRegisterComponent } from './instruction-register.component';

describe('InstructionRegisterComponent', () => {
  let component: InstructionRegisterComponent;
  let fixture: ComponentFixture<InstructionRegisterComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [InstructionRegisterComponent]
    });
    fixture = TestBed.createComponent(InstructionRegisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
