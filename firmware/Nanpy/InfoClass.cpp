#include "cfg.h"

#if USE_Info

#include "InfoClass.h"
#include <stdlib.h>

const char* nanpy::InfoClass::get_firmware_id()
{
    return "Info";
}

void nanpy::InfoClass::elaborate(nanpy::MethodDescriptor* m)
{
    nanpy::SlimArray <nanpy::BaseClass*> * classes = Register::get_classes();
    if (strcmp(m->getName(), "count") == 0)
    {
        m->returns(classes->getSize());
    }
    if (strcmp(m->getName(), "name") == 0)
    {
        int index = m->getInt(0);
        m->returns(classes->get(index)->get_firmware_id());
    }
}
#endif
