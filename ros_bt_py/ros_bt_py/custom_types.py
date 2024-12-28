# Copyright 2024 FZI Forschungszentrum Informatik
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    * Neither the name of the FZI Forschungszentrum Informatik nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import rosidl_runtime_py
import rosidl_runtime_py.utilities


class FilePath(object):
    def __init__(self, path=''):
        self.path = path


class MathUnaryOperator(object):
    def __init__(self, operator='sqrt'):
        self.operator = operator


class MathBinaryOperator(object):
    def __init__(self, operator='+'):
        self.operator = operator


class MathOperandType(object):
    def __init__(self, operand_type='float'):
        self.operand_type = operand_type


class MathUnaryOperandType(object):
    def __init__(self, operand_type='float'):
        self.operand_type = operand_type


class RosServiceType(object):
    def __init__(self, type_str=''):
        self.type_str = type_str

    @property
    def type_obj(self):
        #NOTE We can't do the conversion in `__init__`,
        # because jsonpickle bypasses the init function.
        return rosidl_runtime_py.utilities.get_service(self.type_str)

#NOTE This should only be used if the service name is specified via options.
# If it is specified via inputs, this would involve unnecessary object creation
class RosServiceName(object):
    def __init__(self, name=''):
        self.name = name