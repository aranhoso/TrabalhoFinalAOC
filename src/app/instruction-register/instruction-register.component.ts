import { Component } from '@angular/core';
import { register } from '../register-file/register';
import { instruction } from './instruction';
import { InstructionToRegisterFileService } from '../services/instruction-to-register-file.service';
import { ProgramMemoryToInstructionService } from '../services/program-memory-to-instruction.service';

@Component({
  selector: 'app-instruction-register',
  templateUrl: './instruction-register.component.html',
  styleUrls: ['./instruction-register.component.scss']
})
export class InstructionRegisterComponent {
    Instruction : instruction = new instruction('00000000010000110010000000000000')
    
    constructor(public InstToRegFile : InstructionToRegisterFileService, public ProgMemToInstReg: ProgramMemoryToInstructionService){}

    SendRegisterNumbers(){    //this sends the 3 register numbers in decimal to the register file instance
      this.InstToRegFile.rd = this.Instruction.ConvertBinToInt(this.Instruction.GetRdRegister()) 
      this.InstToRegFile.rs = this.Instruction.ConvertBinToInt(this.Instruction.GetRsRegister()) 
      this.InstToRegFile.rt = this.Instruction.ConvertBinToInt(this.Instruction.GetRtRegister()) 
    }

}
