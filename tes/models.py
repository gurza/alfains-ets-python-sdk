# -*- coding: utf-8 -*-

"""
tes.models
~~~~~~~~~~
This module contains the primary objects.
"""

from decimal import Decimal
from enum import Enum
import datetime
import uuid

PRODUCT_TYPES = ['AIR']


class ApiProblem:
    """Description of the error that occurred while handling your request."""

    def __init__(self, title=None, status=None, detail=None):
        """Init.

        :param title: Short error description, e.g. 'POLICY_NOT_FOUND'.
        :type title: str or None
        :param status: Status code, e.g. 'PNF_002'.
        :type status: str or None
        :param detail: Full error description,
            e.g. 'Policy with id 12345 not found or does not belong to agent'.
        :type detail: str or None
        """
        self.title = title
        self.status = status
        self.detail = detail


class InsuranceProduct:
    """Insurance product."""

    def __init__(self, code, type=None, description=None, currency=None):
        """Init.

        :param code: Code of insurance product, e.g. 'ON_ANTICOVID_AVIA_1'.
        :type code: str
        :param type: Type of insurance product, one of ``POSSIBLE_PRODUCT_TYPES``, e.g. 'AIR'.
        :type type: str or None
        :param description: Description of insurance product, e.g. 'Страховка от риска медицинских расходов'.
        :type description: str or None
        :param currency: (obsolete) Currency code of the product, ISO 4217, e.g. 'RUB'.
        :type currency: str or None
        """
        self.code = code
        self.type = type
        self.description = description
        self.currency = currency


class Amount:
    """Amount."""

    def __init__(self, value, currency=None):
        """Init.

        :param value: Value, e.g. 35000.
        :type value: Decimal
        :param currency: Currency code, ISO 4217, e.g. 'RUB'.
        :type currency: str or None
        """
        self.value = value
        self.currency = currency


class PolicyStatus:
    pass


class Operator:
    pass


class Agent:
    """Agent."""

    def __init__(self, code, sub=None):
        """Init.

        :param code: Agent code, e.g. 'TestTravelFlightAgent'.
        :type code: str
        :param sub: Subagent.
            The subagent code is used to split sales across different channels or divisions within the same agent.
        :type sub: SubAgent or None
        """
        self.code = code
        self.sub = sub


class SubAgent:
    pass


class Cancellation:
    pass


class ServiceCompany:
    pass


class Person:
    """Person."""

    def __init__(self, first_name=None, last_name=None, patronymic=None,
                 nick_name=None, gender=None, birth_date=None, email=None,
                 address=None, infant=None, nationality=None, id_card=None,
                 phone=None, document=None, ticket=None, risks=None):
        """Init.

        :param first_name: First name, e.g. 'Федор'.
        :type first_name: str or None
        :param last_name: Last name, e.g. 'Васильев'.
        :type last_name: str or None
        :param patronymic: Patronymic, e.g. 'Иванович'.
        :type patronymic: str or None
        :param nick_name: Nick, e.g. 'Васильев Федор Иванович'.
        :type nick_name: str or None
        :param gender: Gender.
        :type gender: Gender or None
        :param birth_date: Birth date.
        :type birth_date: datetime.date
        :param email: Email, e.g. 'fedor.vasilyev@email.com'.
        :type email: str or None
        :param address: Address, e.g. 'г. Москва, ул. Иванова, д. 4, кв. 198'.
        :type address: str or None
        :param infant: True if the person is an infant.
        :type infant: bool or None
        :param nationality: Code of country, ISO 3166-1, e.g. 'RU'.
        :type nationality: str or None
        :param id_card: Number of additional document ID, e.g. '5456876321656'.
        :type id_card: str or None
        :param phone: Contact phone.
        :type phone: Phone or None
        :param document: Document ID.
        :type document: Document or None
        :param ticket: Ticket information.
        :type ticket: Ticket or None
        :param risks: Information about risks.
        :type risks: list[Risk] or None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.nick_name = nick_name
        self.gender = gender
        self.birth_date = birth_date
        self.email = email
        self.address = address
        self.infant = infant
        self.nationality = nationality
        self.id_card = id_card
        self.phone = phone
        self.document = document
        self.ticket = ticket
        self.risks = risks if risks is not None else []


class Phone:
    """Phone."""

    def __init__(self, number=None, type=None):
        """Init.

        :param number: Phone number, e.g. '89101234567'.
        :type number: str or None
        :param type: Phone type.
        :type type: PhoneType or None
        """
        self.number = number
        self.type = type


class Document:
    """Document ID."""

    def __init__(self, type=None, number=None, country=None):
        """Init.

        :param type: Document type.
        :type type: DocumentType or None
        :param number: Document number, e.g. '2901178356'.
        :type number: str or None
        :param country: Code of the country where the document was issued, ISO 3166-1, e.g. 'RU'.
        :type country: str or None
        """
        self.type = type
        self.number = number
        self.country = country


class Ticket:
    """Ticket."""

    def __init__(self, number=None, price=None, issue_date=None):
        """Init.

        :param number: Ticket number, e.g. '5723574320584'.
        :type number: str or None
        :param price: Ticket price.
        :type price: Amount or None
        :param issue_date: Issue date.
        :type issue_date: datetime.date or None
        """
        self.number = number
        self.price = price
        self.issue_date = issue_date


class Risk:
    """Risk."""

    def __init__(self, type=None, coverage=None, franchise=None):
        """Init.

        :param type: Risk type.
        :type type: RiskType or None
        :param coverage: Insurance amount.
        :type coverage: Amount or None
        :param franchise: Franchise amount.
        :type franchise: Amount or None
        """
        self.type = type
        self.coverage = coverage
        self.franchise = franchise


class Segment:
    """Travel segment."""

    def __init__(self, transport_operator_code=None, route_number=None, service_class=None,
                 connection_time=None, departure=None, arrival=None, place_number=None,
                 car_number=None, car_type=None, connecting_flight=None, flight_direction=None):
        """Init.
        
        :param transport_operator_code: Carrier code, e.g. 'SU'.
        :type transport_operator_code: str or None
        :param route_number: Route number (flight number, train number, etc), e.g. '1490'.
        :type route_number: str or None
        :param service_class: Service class.
        :type service_class: ServiceClass or None
        :param connection_time: Connection time in minutes, e.g. 120.
        :type connection_time: int or None
        :param departure: Departure point.
        :type departure: Point or None
        :param arrival: Arrival point.
        :type arrival: Point or None
        :param place_number: Place or seat number, e.g. '56b'.
        :type place_number: str or None
        :param car_number: Train car number, e.g. '12'.
        :type car_number: str or None
        :param car_type: Train car type, e.g. 'SV'.
        :type car_type: str or None
        :param connecting_flight: True if flight is connecting.
        :type connecting_flight: bool or None
        :param flight_direction: Flight direction.
        :type flight_direction: FlightDirection or None
        """
        self.transport_operator_code = transport_operator_code
        self.route_number = route_number
        self.service_class = service_class
        self.connection_time = connection_time
        self.departure = departure
        self.arrival = arrival
        self.place_number = place_number
        self.car_number = car_number
        self.car_type = car_type
        self.connecting_flight = connecting_flight
        self.flight_direction = flight_direction


class TravelType:
    pass


class Point:
    """Departure or arrival point."""

    def __init__(self, date=None, point=None, country=None):
        """Init.

        :param date: Datetime of departure/arrival.
        :type date: datetime.datetime or None
        :param point: Code of departure/arrival point, e.g. 'SVO'.
        :type point: str or None
        :param country: Code of country, ISO 3166-1, e.g. 'RU'.
        :type country: str or None
        """
        self.date = date
        self.point = point
        self.country = country


class Gender(Enum):
    """Gender."""

    MALE = 1
    FEMALE = 2


class PhoneType(Enum):
    """Phone type"""

    MOBILE = 1
    HOME = 2
    OFFICE = 3
    OTHER = 4


class DocumentType(Enum):
    """Document type."""

    PASSPORT = 1
    INTERNATIONAL = 2
    IDCARD = 3
    MILITARY = 4
    FOREIGNER = 5
    JURIDICAL = 6
    ERGUL = 7
    DRIVER_LICENCE = 8
    BIRTHCERTIFICATE = 9


class RiskType(Enum):
    """Risk type."""

    RISK_MR = 1
    RISK_NSP = 2
    RISK_NS = 3
    RISK_FLIGHT_DELAYS_PERSONAL = 4
    RISK_SPORT = 5
    RISK_LOSS_LUGGAGE_PERSONAL = 6
    RISK_DELAYED_LUGGAGE_PERSONAL = 7
    RISK_GO = 8
    RISK_LUGGAGE_MASSIVE = 9
    RISK_FLIGHT_DELAYS_MASSIVE = 10
    RISK_NR = 11
    RISK_PROPERTY = 12
    RISK_EVENT = 13
    RISK_LOSS_RESTORE_DOCUMENTS = 14
    RISK_CL = 15
    RISK_LUGGAGE_DAMAGE = 16
    RISK_COVID = 17


class FareType:
    pass


class LuggageType:
    pass


class Opt(Enum):
    """Option state."""

    OPT_IN = 1
    OPT_OUT = 2
    SMART_OPT_IN = 3
    SMART_OPT_OUT = 4


class SellingPage(Enum):
    """Selling page."""

    CROSS_SALE = 1
    BOOKING_EDITION = 2
    WEB_CHECK_IN = 3
    STANDALONE = 4


class FlightDirection(Enum):
    """Flight direction."""

    OW = 1  # One way
    RT = 2  # Round trip


class AcquisitionChannel(Enum):
    """Acquisition (data collection) channel."""

    DESKTOP = 1
    MOBILE_SITE = 2
    MOBILE_APP = 3


class Policy:
    """Insurance policy."""

    def __init__(self, policy_id=None, product=None, insured=None,
                 insurer=None, customer_email=None, customer_phone=None, pnr=None,
                 series=None, payment_type=None, sale_session=None, issuance_city=None,
                 external_id=None, commentary=None, description=None, resources=None,
                 travel_type=None, sport=None, service_company=None, segments=None,
                 ticket=None, rate=None, discounted_rate=None, begin_date=None,
                 end_date=None, period_of_validity=None, risks=None, status=None,
                 created_at=None, update_at=None, fare_type=None, luggage_type=None,
                 fare_code=None, cancellation=None, operator=None, agent=None,
                 manager_name=None, manager_code=None, opt=None, selling_page=None,
                 service_class=None, age_group=None, acquisition_channel=None, error=None):
        """Init.

        :param policy_id:
        :param product:
        :param insured:
        :param insurer:
        :param customer_email:
        :param customer_phone:
        :param pnr:
        :param series:
        :param payment_type:
        :param sale_session:
        :param issuance_city:
        :param external_id:
        :param commentary:
        :param description:
        :param resources:
        :param travel_type:
        :param sport:
        :param service_company:
        :param segments:
        :param ticket:
        :param rate:
        :param discounted_rate:
        :param begin_date:
        :param end_date:
        :param period_of_validity:
        :param risks:
        :param status:
        :param created_at:
        :param update_at:
        :param fare_type:
        :param luggage_type:
        :param fare_code:
        :param cancellation:
        :param operator:
        :param agent: Agent who owns this policy.
        :type agent: Agent or None
        :param manager_name: Manager (cashier) code, e.g. 'Ivanova A.A.'.
        :type manager_name: str or None
        :param manager_code: Manager (cashier) code, e.g. '1q2w3e4r'.
        :type manager_code: str or None
        :param opt: Option state.
        :type opt: Opt or None
        :param selling_page: Policy selling page.
        :type selling_page: SellingPage or None
        :param service_class: Service class.
        :type service_class: ServiceClass or None
        :param age_group: Age group, e.g. '0-75'.
        :type age_group: str or None
        :param acquisition_channel: Acquisition (data collection) channel.
        :type acquisition_channel: AcquisitionChannel or None
        :param error: Error message.
        :type error: str or None
        """
        self.manager_name = manager_name
        self.manager_code = manager_code
        self.opt = opt
        self.selling_page = selling_page
        self.service_class = service_class
        self.age_group = age_group
        self.acquisition_channel = acquisition_channel
        self.error = error


class Declaration:
    pass


class QuoteRequest:
    """Request for calculating one or more insurance policies."""

    def __init__(self, session_id=None, product=None, insureds=None,
                 segments=None, booking_price=None, currency=None, service_class=None,
                 country=None):
        """Init.

        :param session_id: Session id, e.g. '88c70099-8e11-4325-9239-9c027195c069'.
        :type session_id: str or None
        :param product: Insurance product.
        :type product: InsuranceProduct or None
        :param insureds: List of insured persons.
        :type insureds: list[Person] or None
        :param segments: List of travel segments, e.g. list of flights.
        :type segments: list[Segment]
        :param booking_price: Total price of the booking.
        :type booking_price: Amount or None
        :param currency: Quote currency code, ISO 4217, e.g. 'RUB'.
        :type currency: str or None
        :param service_class: Service class.
        :type service_class: ServiceClass or None
        :param country: Country code where the insurance policy will be paid for, ISO 3166-1, e.g. 'RU'.
        :type country: str or None
        """
        self.session_id = session_id if session_id is not None else str(uuid.uuid4())
        self.product = product
        self.insureds = insureds if insureds is not None else []
        self.segments = segments if segments is not None else []
        self.booking_price = booking_price
        self.currency = currency
        self.service_class = service_class
        self.country = country


class QuoteResponse:
    """Quote response."""

    def __init__(self, session_id=None, quotes=None):
        """Init.

        :param session_id: Session id, e.g. '88c70099-8e11-4325-9239-9c027195c069'.
        :type session_id: str or None
        :param quotes: List of policies for each insured person.
        :type quotes: list[Quote] or None
        """
        self.session_id = session_id
        self.quotes = quotes if quotes is not None else []


class Quote:
    """Quote/Calculating."""

    def __init__(self, policies=None, error=None):
        """Init.

        :param policies: List of policies.
        :type policies: list[Policy]
        :param error: Policy calculating error.
        :type error: str or None
        """
        self.policies = policies if policies is not None else []
        self.error = error


class CreateRequest:
    pass


class CreateResponse:
    pass


class UpdateRequest:
    pass


class UpdateResponse:
    pass


class ConfirmRequest:
    pass


class SaleWithoutInsuranceRequest:
    pass


class SaleWithoutInsuranceResponse:
    pass


class ServiceClass(Enum):
    """Service class."""

    ECONOM = 1
    COMFORT = 2
    BUSINESS = 3
