import { TestBed } from '@angular/core/testing';

import { RegisterFileToALUService } from './register-file-to-alu.service';

describe('RegisterFileToALUService', () => {
  let service: RegisterFileToALUService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RegisterFileToALUService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
