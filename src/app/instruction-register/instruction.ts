export class instruction{
    Instruction:string;

    constructor(inst:string){
        this.Instruction = inst
    }

    ConvertBinToInt(num:string){    //this function is going to take the register number in binary and convert to int so we can send to register-file with service
        let num2 = parseInt(num,2)
        return num2
    }

    GetOpCode():string{
        let opCode:string = ''
        for(let i=0; i<6; i++){
            opCode = opCode + this.Instruction.charAt(i)
        }
        return opCode
    }

    GetRdRegister():string{
        let RdRegister:string = ''
        for(let i=6; i<11; i++){
            RdRegister = RdRegister + this.Instruction.charAt(i)
        }
        return RdRegister
    }

    GetRsRegister():string{
        let RsRegister:string = ''
        for(let i=11; i<16; i++){
            RsRegister = RsRegister + this.Instruction.charAt(i)
        }
        return RsRegister
    }

    GetRtRegister():string{
        let RtRegister:string = ''
        for(let i=16; i<21; i++){
            RtRegister = RtRegister + this.Instruction.charAt(i)
        }
        return RtRegister
    }
    GetShamt(){
        let Shamt:string = ''
        for(let i=21; i<26; i++){
            Shamt = Shamt + this.Instruction.charAt(i)
        }
        return Shamt
    }

    GetFunc(){
        let Func:string = ''
        for(let i=26; i<32; i++){
            Func = Func + this.Instruction.charAt(i)
        }
        return Func
    }

    Get26BitExtended(){         //for jump instruction
        let Extended26bit:string = ''
        for(let i=6; i<32; i++){
            Extended26bit = Extended26bit + this.Instruction.charAt(i)
        }
        return Extended26bit
    }

    Get16BitExtended(){         //for jump instruction
        let Extended16bit:string = ''
        for(let i=16; i<32; i++){
            Extended16bit = Extended16bit + this.Instruction.charAt(i)
        }
        return Extended16bit
    }

    GetByte(byte:number):string{
        let byteStr: string = ''
        switch(byte){
            case 1:
            for(let i=0; i<8; i++){
                byteStr = byteStr + this.Instruction.charAt(i)
            }
            return byteStr
            break
            case 2:
            for(let i=8; i<16; i++){
                byteStr = byteStr + this.Instruction.charAt(i)
            }
            return byteStr
            break
            case 3:
            for(let i=16; i<24; i++){
                byteStr = byteStr + this.Instruction.charAt(i)
            }
            return byteStr
            break
            case 4:
            for(let i=24; i<32; i++){
                byteStr = byteStr + this.Instruction.charAt(i)
            }
            return byteStr
            break
            default:
            return byteStr
            break
        }
    }
}