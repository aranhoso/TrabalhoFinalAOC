import { Component } from '@angular/core';
import { register } from '../register-file/register';
import { RegisterFileToALUService } from '../services/register-file-to-alu.service';

@Component({
  selector: 'app-alu',
  templateUrl: './alu.component.html',
  styleUrls: ['./alu.component.scss']
})
export class ALUComponent {

  constructor(public RegFileToALU: RegisterFileToALUService){}

  A: register = new register()
  B: register = new register()
  Zero : register = new register()
  Result : register = new register()

  GetRegFileOperands(){
    this.A = this.RegFileToALU.ReadData1
    this.B = this.RegFileToALU.ReadData2
    window.alert("THIS IS TEST FOR REGISTER FILE TO ALU SERVICE"+"\nA operand: "+this.A.Decimal+"\nB operand:"+this.B.Decimal)
  }


  
  }

