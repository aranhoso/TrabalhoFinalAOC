import { TestBed } from '@angular/core/testing';

import { InstructionToRegisterFileService } from './instruction-to-register-file.service';

describe('InstructionToRegisterFileService', () => {
  let service: InstructionToRegisterFileService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InstructionToRegisterFileService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
