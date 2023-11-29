import { Component, Input, OnInit } from '@angular/core';
import { register } from './register';
import { instruction } from '../instruction-register/instruction';
import { InstructionToRegisterFileService } from '../services/instruction-to-register-file.service';
import { RegisterFileToALUService } from '../services/register-file-to-alu.service';

@Component({
  selector: 'app-register-file',
  templateUrl: './register-file.component.html',
  styleUrls: ['./register-file.component.scss']
})
export class RegisterFileComponent implements OnInit {

  constructor(public InstToRegFile:InstructionToRegisterFileService,
              public RegFileToALU: RegisterFileToALUService
            ){}
  
  RegisterValues:register[] = [];
  rd: number = 0 //will come from InstructionToRegisterFile service
  rs: number = 0 //will come from InstructionToRegisterFile service
  rt: number = 0 //will come from InstructionToRegisterFile service
  WriteData = new register();
  ReadData1 = new register();
  ReadData2 = new register();
  
  btnClick(){   //assign the register numbers that are located in the service to here so that our component can use them in practice
    this.rd = this.InstToRegFile.rd
    this.rs = this.InstToRegFile.rs
    this.rt = this.InstToRegFile.rt
    window.alert("THIS IS TEST FOR INSTRUCTION REGISTER TO REGISTER FILE SERVICE\nrd: "+this.rd+
    "\nrs: "+this.rs+
    "\nrt: "+this.rt)
  }

  SetAluOperands(){  //this sends data  to ALU to process (referent to R format instructions)
    this.RegFileToALU.ReadData1 = this.ReadData1
    this.RegFileToALU.ReadData2 = this.ReadData2
  }

  ngOnInit(): void {
    for(let i=0; i<32; i++){
    this.RegisterValues.push(new register())
    }

    //this should be erased later on
    this.RegisterValues[3].Decimal = 77
    this.RegisterValues[4].Decimal = 84
    
  }

  
  /*setReadDataFields(opCode:number,rdIndex:number, rsIndex:number, rtIndex:number, shamt:number, funcCode:number ){
    switch(opCode){
      case 1:  //opCode = 1 indica operações aritméticas
        switch(funcCode){
          case 1: //funcCode = 1 indica soma
          this.ReadData1 = this.RegisterValues[rsIndex]
          this.ReadData2 = this.RegisterValues[rtIndex] 
          this.ArithmeticResultIndex = rdIndex;
        }
    }
  }*/
  SetReadDataFields(){
    this.ReadData1 = this.RegisterValues[this.rs]
    this.ReadData2 = this.RegisterValues[this.rt]
  }

  public static ToBinary32(num: number):string{
    return (num >>> 0).toString(2);
  }
}
