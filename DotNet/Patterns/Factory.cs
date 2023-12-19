
using System;

namespace Patterns
{

    interface IUserNotifier
    {
        void NotifyUser(int id);
    }

    class EmailNotifier : IUserNotifier
    {
        public void NotifyUser(int id)
        {
            Console.WriteLine($"Notify User {id} By Email");
        }
    }

    class TestUserNotifier : IUserNotifier
    {
        public void NotifyUser(int id)
        {
            Console.WriteLine($"Pretending to notify User {id}");
        }
    }

    class NotificationServiceProvider
    {
        public IUserNotifier GetUserNotifier()
        {
#if Debug
                return new TestUserNotifier();
#else
            return new EmailNotifier();
#endif
        }
    }

    class ShippingService {
        NotificationServiceProvider _serviceProvider;

        public ShippingService(NotificationServiceProvider serviceProvider)
        {
            _serviceProvider = serviceProvider;
        }

        public void ShipItem()
        {
            _serviceProvider.GetUserNotifier().NotifyUser(1);
        }
    }

}
